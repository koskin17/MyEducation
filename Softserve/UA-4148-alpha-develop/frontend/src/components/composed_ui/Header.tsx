import { Navigation } from "./Navigation";
import { AuthButtons } from "./AuthButtons";
import { Logo } from "./Logo";
import { Search } from "../composed/Search";
import { useDesktop } from "@/hooks/useDesktop";
import { MenuIcon } from "@/icons/MenuIcon";
import { cn } from "@/libs/utils";
import { Button } from "../ui/button";
import { XIcon } from "@/icons/XIcon";
import { useModal } from "@/hooks/useModal";

export const Header = () => {
  const isDesktop = useDesktop();
  const modal = useModal();

  return (
    <header className="bg-main-white border-b border-inactive-60 flex flex-col fixed top-0 left-0 right-0">
      <div
        className={cn(
          "flex justify-between w-full max-w-[1304px] py-4 mx-auto z-50 relative",
          {
            "px-6": isDesktop,
            "px-4": !isDesktop,
          }
        )}
      >
        <Logo />
        <div className="flex items-center gap-6">
          {isDesktop && (
            <>
              <Navigation />
              <Search />
            </>
          )}
          <div className="flex items-center gap-6">
            <AuthButtons />
            {!isDesktop && (
              <Button
                aria-label={modal.isOpen ? "Close menu" : "Open menu"}
                onClick={modal.toggle}
                variant={"tertiary"}
              >
                {modal.isOpen ? <XIcon /> : <MenuIcon />}
              </Button>
            )}
          </div>
        </div>
      </div>
      {modal.isOpen && (
        <div
          role="dialog"
          aria-modal="true"
          className="bg-main-white z-40 inset-0 h-screen border-t border-inactive-60 px-6 py-8 flex flex-col gap-6"
        >
          <Search onSubmit={modal.toggle} />
          <Navigation onClick={modal.toggle} className="flex-col items-start" />
        </div>
      )}
    </header>
  );
};
